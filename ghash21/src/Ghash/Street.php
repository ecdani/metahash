<?php
namespace Ghash;

class Street {
  public $start; // B
  public $end; // E
  public $name; // the street name (a string consisting of between 3 and 30 lowercase ASCII characters a - z and the character - ),
  public $time; // L

  public function __construct($start, $end, $name, $time) {
    $this->start = $start; // intersección desde
    $this->end = $end; // intersección hasta
    $this->name = $name;
    $this->time = $time;

    // echo "start: $this->start" . PHP_EOL;
    // echo "end: $this->end" . PHP_EOL;
    // echo "name: $this->name" . PHP_EOL;
    // echo "time: $this->time" . PHP_EOL;
  }
}
