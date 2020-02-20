<?php

namespace Ghash;

class Idiot extends Problem {

/**
 * here~
 *  2 # Dos librerias vamos a scanear
 *  0 3 #libreria 0#  #3libros para scanear#
 *  1 2 3 #los libros que vamos a mandar (score)
 *  1 2 #otra libreria
 *  4 5
 */
  public function writeSolution(string $filename): self {
    $booksScanned = [];
    $handle = fopen(self::OUT_PATH . $filename, 'w');

    fwrite($handle, $this->totalLibraries . "\n");
    foreach ($this->libraries as $key => $library) {
      $booksToScanArray = array_filter($library->books, function ($bookKey) use (&$booksScanned) {
        if (!in_array($bookKey, $booksScanned)) {
          $booksScanned[] = $bookKey;
          return true;
        }
        return false;
      });

      $output = '';
      $output .= $library->id . ' ' . count($booksToScanArray);
      fwrite($handle, $output . "\n");
      fwrite($handle, implode(' ', $booksToScanArray));
    }

    fclose($handle);

    return $this;
  }
}
