<?php
declare(strict_types=1);
/* Schedule from the webhost CLI, never expose an HTTP maintenance operation. */
if (PHP_SAPI !== 'cli') { http_response_code(405); exit; }
require __DIR__ . '/_runtime.php';
try {
    if (($argv[1] ?? '') !== '--purge-expired') throw new RuntimeException('Use --purge-expired');
    $cfg = wm_config(); $days = $cfg['retention_days'] ?? 30;
    if (!is_int($days) || $days < 1 || $days > 365) throw new RuntimeException('Invalid retention');
    $cutoff = time() - $days * 86400; $removed = 0;
    foreach (glob($cfg['_data'] . '/inbound-*.json') as $path) {
        if (!is_link($path) && preg_match('/^inbound-[a-f0-9]{32}\.json$/D', basename($path)) && filemtime($path) < $cutoff) { unlink($path); $removed++; }
    }
    wm_store($cfg, 'newsletter', function(array &$state) use ($cutoff): void {
        foreach ($state as $id => $entry) if (($entry['state'] === 'pending' && ($entry['expires'] ?? 0) < time()) || ($entry['state'] === 'unsubscribed' && strtotime($entry['unsubscribed_at']) < $cutoff)) unset($state[$id]);
    });
    $retention = $cfg['analytics']['retention_days'] ?? 30;
    if (!is_int($retention) || $retention < 1 || $retention > 365) throw new RuntimeException('Invalid retention');
    $dayCutoff = gmdate('Y-m-d', time() - ($retention - 1) * 86400);
    wm_store($cfg, 'analytics', function(array &$state) use ($dayCutoff): void { $state = array_filter($state, fn($day) => $day >= $dayCutoff, ARRAY_FILTER_USE_KEY); });
    wm_store($cfg, 'rate', function(array &$state): void { $state = array_filter($state, fn($entry) => ($entry['expires'] ?? 0) > time()); });
    echo json_encode(['status'=>'local_retention_applied','outbox_records_removed'=>$removed], JSON_THROW_ON_ERROR) . "\n";
} catch (Throwable $error) { fwrite(STDERR, "WEBMODULE_MAINTENANCE_BLOCKED\n"); exit(2); }
