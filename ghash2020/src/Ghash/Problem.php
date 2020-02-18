<?php

namespace Ghash;

class Problem {
  const OUT_PATH = __DIR__ . '/../../out';

  public function parse(string $filename): self {
    $handle = fopen($filename, 'r');
    while (($line = fgets($handle)) !== false) {
      // TODO: Parseo aquí
    }
    fclose($handle);

    return $this;
  }

  public function resolve(): self {
    return $this;
  }

  public function writeSolution(string $filename): self {
    return $this;
  }
}
