<?php

namespace Ghash;

class Idiot extends Problem {

  /**
   *
   */
  public function writeSolution(string $filename): self {
    $handle = fopen(self::OUT_PATH . $filename, 'w');

    fwrite($handle, count($this->masterplan) . "\n");
    foreach ($this->masterplan as $key => $schedule) {
      $schedule->printSchedule($handle);
    }

    fclose($handle);

    return $this;
  }
}
