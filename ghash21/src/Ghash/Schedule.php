<?php
namespace Ghash;

/**
 * Planificación del conjunto de semaforos de un cruze
 */
class Schedule {
  public $intersection; // i
  public $nStreets; // E_i   <- ES CALCULADO
  public $plans; // F
  public $key; // La key perdida

  public function __construct($intersection, $key, $plans) {
    $this->intersection = $intersection;
    $this->plans = $plans; // array objectos Encendidos
    $this->key = $key;
  }

  public function printSchedule($handle) {
    fwrite($handle, $this->key . "\n");
    fwrite($handle, $this->totalStreets() . "\n");
    foreach ($this->plans as $plan) {
      fwrite($handle, $plan->street->name . ' ' . $plan->time . "\n");
    }
  }

  public function totalStreets() {
    $streetsCounted = [];
    $totalStreets = 0;
    foreach ($this->plans as $plan) {
      if (!in_array($plan->street->name, $streetsCounted)) {
        $streetsCounted[] = $plan->street->name;
        $totalStreets++;
      }
    }
    return $totalStreets;
  }

}
