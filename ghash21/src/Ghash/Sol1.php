<?php

namespace Ghash;

/**
 * Semaforos rotativos
 */
class Sol1 extends Idiot
{

  public $masterplan = []; // conjunto de plans

  /**
   * public $time;
   * public $intersections;
   * public $totalStreets;
   * public $cars;
   * public $scorePerCar;
   * public $streets = [];
   * public $carRoutes = [];
   *
   */
  public function resolve(): self {
    // -1 si a es menor (que b)
    $encendidos = []; // plans

    //public $incomingStreets = [];
    //public $outcomingStreets = [];

    foreach ($this->intersections as $key => $intersection) {
      foreach ($intersection->incomingStreets as $keyStreet => $street) {
        $encendidos[] = new Encendido($street, 1);
      }
      $this->masterplan[] = new Schedule($intersection, $key, $encendidos);
      $encendidos = [];
    }

    //usort($this->libraries, function ($a, $b) {
    //  if ($a->booksPerDay == $b->booksPerDay) {
    //    return 0;
    //  }
//
    //  return ($a->booksPerDay > $b->booksPerDay) ? -1 : 1;
    //});

    return $this;
  }
}
