<?php

namespace Ghash;

class Problem {
  const OUT_PATH = __DIR__ . '/../../out/';

  public function parse(string $filename): self {
    $handle = fopen($filename, 'r');

    // TODO

    fclose($handle);

    return $this;
  }

  public function resolve(): self {
    return $this;
  }

  public function writeSolution(string $filename): self {
    // $handle = fopen($filename, 'w');

    //fwrite($handle, 'meh');

    // fclose($handle);

    return $this;
  }
}
