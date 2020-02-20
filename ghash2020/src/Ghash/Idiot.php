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
    $handle = fopen($filename, 'w');
    
    fwrite($handle, $totalLibraries . "\n");
    foreach ($this->libraries as $key => $library) {
      $output = '';
      $output .= $library->id . ' ' . $library->totalBooks;
      fwrite($handle, $output . "\n");
      $output = '';
      foreach ($library->books as $key => $book) {
        $output .= $key . ' ';
      }
      fwrite($handle, $output . "\n");
    }

    //fwrite($handle, 'meh');

    fclose($handle);

    return $this;
  }
}
