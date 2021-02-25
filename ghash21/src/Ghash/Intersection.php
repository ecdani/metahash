<?php
namespace Ghash;

class Intersection {
  public $incomingStreets = [];
  public $outcomingStreets = [];

  public function __construct() {
    // $this->incomingStreets = $incomingStreets;
    // $this->outcomingStreets = $outcomingStreets;
  }

  /**
   * 0 = incoming
   * 1 = outcoming
   */
  public function addStreet($street, $type) {
    if ($type == 0) {
      $this->incomingStreets[] = $street;
    } else {
      $this->outcomingStreets[] = $street;
    }
  }

}
