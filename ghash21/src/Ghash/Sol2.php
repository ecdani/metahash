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

    /*
    public $totalStreets; // P
    public $streets; // Calles en orden (array de strings)
    public $time; // D
    public $scorePerCar; // F

    public $tiempoRecorridoMinimo;
    public $scoreMaximo;

    */
    //foreach ($this->cars as $key => $car) {
      // -1 si a es menor (que b)
      usort($this->cars, function ($a, $b) {
        if ($a->booksPerDay == $b->booksPerDay) {
          return 0;
        }

        return ($a->scoreMaximo < $b->scoreMaximo) ? -1 : 1;
      });
    //}

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
