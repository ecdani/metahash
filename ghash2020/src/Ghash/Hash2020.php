<?php

namespace Ghash;

class Hash2020 {
  const IN_PATH = __DIR__ . '/../../in/';

  public static function resolve(string $filename): void {
    $problem = new Problem();
    $problem->parse(self::IN_PATH . $filename);
    $problem->resolve();
    $problem->writeSolution($filename);
  }

  public static function resolveAll(): void {
    foreach (scandir(self::IN_PATH) as $filename) {
      if (substr( $filename, 0, 1 ) === '.') {
        continue;
      }
      echo "Resolviendo $filename..." . PHP_EOL;
      self::resolve($filename);
      echo "$filename resuelto." . PHP_EOL;
    }
  }
}
