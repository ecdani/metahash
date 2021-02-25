<?php

namespace Ghash;

class Problem {
  const OUT_PATH = __DIR__ . '/../../out/';

  public $time;
  public $nIntersections;
  public $totalStreets;
  public $cars;
  public $scorePerCar;
  public $streets = [];
  public $carRoutes = [];
  public $intersections = [];

  public function parse(string $filename): self {
    $handle = fopen($filename, 'r');

    // 1ª línea
    $line = fgets($handle);
    list($this->time, $this->nIntersections, $this->totalStreets, $this->cars, $this->scorePerCar) = explode(' ', $line);

    for ($i = 0; $i < $this->nIntersections; $i++) {
      $this->intersections[] = new Intersection();
    }

    // Líneas de calles
    for ($i = 0;$i < $this->totalStreets; $i++) {
      $line = fgets($handle);
      $vars = explode(' ', $line);
                            //Start, end
      $street = new Street($vars[0], $vars[1], $vars[2], $vars[3]);
      $this->streets[] = $street;
      $this->intersections[$vars[0]]->addStreet($street, 1);
      $this->intersections[$vars[1]]->addStreet($street, 0);
    }

    // Líneas de rutas de coches
    while (($line = fgets($handle)) !== false) {
      $lineArray = explode(' ', $line);
      $streets = array_shift($lineArray);
      $this->carRoutes[] = new Car($streets, $this->findStreetsByName($lineArray), $this->time, $this->scorePerCar);
    }

    // echo 'Segundos: ' . $this->time . PHP_EOL;
    // echo 'Intersecciones: ' . $this->nIntersections . PHP_EOL;
    // echo 'Total de calles: ' . $this->totalStreets . PHP_EOL;
    // echo 'Coches: ' . $this->cars . PHP_EOL;
    // echo 'Puntuación por coche: ' . $this->scorePerCar . PHP_EOL;
    // echo 'Calles: ' . PHP_EOL;
    // print_r($this->streets);
    // echo PHP_EOL;
    // echo 'Rutas: ' . PHP_EOL;
    // print_r($this->carRoutes);
    // echo PHP_EOL;
    // die();

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

  protected function findStreetsByName(array $streetNames): array {
    return array_map(function (string $streetName) {
      $streetName = rtrim($streetName, "\n");
      foreach ($this->streets as $street) {
        if ($street->name == $streetName) {
          return $street;
        }
      }
    }, $streetNames);
  }
}
