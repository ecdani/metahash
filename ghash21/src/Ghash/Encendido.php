<?php
namespace Ghash;

class Encendido {
  public $street;
  public $time; // T

  public function __construct($street, $time) {
    $this->street = $street; /// Transformar a objeto? -> Pasaré un objeto calle.
    $this->time = $time;

  }

}
