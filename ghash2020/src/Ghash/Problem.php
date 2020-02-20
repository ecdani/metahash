<?php

namespace Ghash;

class Problem {
  const OUT_PATH = __DIR__ . '/../../out/';

  public static $totalBooks;
  public static $totalLibraries;
  public static $totalDays;
  public static $bookScores;
  public $libraries = [];

  public function parse(string $filename): self {
    $handle = fopen($filename, 'r');

    // 1ª línea
    $line = fgets($handle);
    list($this->totalBooks, $this->totalLibraries, $this->totalDays) = explode(' ', $line);

    // 2ª línea
    $line = fgets($handle);
    $this->bookScores = explode(' ', $line);

    // echo "Total de libros: $this->totalBooks" . PHP_EOL;
    // echo "Total de bibliotecas: $this->totalLibraries" . PHP_EOL;
    // echo "Total de días: $this->totalDays" . PHP_EOL;
    // echo "Puntuaciones de los libros:" . PHP_EOL;
    // print_r($this->bookScores);

    $lineNumber = 3;
    $libraryId = 0;
    while (($line = fgets($handle)) !== false) {
      // Datos biblioteca
      if ($lineNumber % 2 == 1) {
        list($libraryTotalBooks, $libraryDaysToSign, $libraryBooksPerDay) = explode(' ', $line);

        $lineNumber++;
        continue;
      }

      // Libros en la biblioteca
      $libraryBooks = explode(' ', $line);

      // Instanciar biblioteca
      $this->libraries[] = new Library($libraryTotalBooks, $libraryDaysToSign, $libraryBooksPerDay, $libraryBooks, $libraryId);
      $lineNumber++;
      $libraryId++;
    }

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
