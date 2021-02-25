<?php
namespace Ghash;

class Car {
  public $totalStreets; // P
  public $streets; // Calles en orden (array de strings)
  public $time; // D
  public $scorePerCar; // F

  public $tiempoRecorridoMinimo;
  public $scoreMaximo;

  public function __construct($totalStreets, $streets, $time, $scorePerCar) {
    $this->totalStreets = $totalStreets;
    $this->streets = $streets;
          /**
           *     $this->start = $start; // intersección desde
         * $this->end = $end; // intersección hasta
         * $this->name = $name;
         * $this->time = $time;
           */
    $this->time = $time;
    $this->scorePerCar = $scorePerCar;

    $this->getTiempoRecorridoMinimo();
    $this->getScoreMaximo();
    // echo "Total de calles: $this->totalStreets" . PHP_EOL;
    // echo "Calles: $this->streets" . PHP_EOL;
    // print_r($this->streets);
  }

  public function getTiempoRecorridoMinimo() {
    foreach ($this->streets as $key => $street) {
      $this->tiempoRecorridoMinimo += $street->time;
    }
  }

  public function getScoreMaximo() {
    $this->scoreMaximo = $this->scorePerCar + ($this->time - $this->tiempoRecorridoMinimo);
  }

  public function getCarScore() {
    //return array_reduce(array_filter($this->bookScores, function($book, $index) {
    //  return in_array($index, $this->books);
    //  }), function($sum, $a) {
    //    return $sum + $a;
    //  }, 0);
  }

  /**
   * Ordenados los coches por score
   */
  public function sortedLibrary() {
    //usort($this->books, function ($a, $b) {
    //  if ($this->bookScores[$a] == $this->bookScores[$b]) {
    //    return 0;
    //  }
//
    //  return ($this->bookScores[$a] > $this->bookScores[$b]) ? -1 : 1;
    //});
  }
}
