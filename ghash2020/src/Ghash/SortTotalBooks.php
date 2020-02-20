<?php

namespace Ghash;

class SortTotalBooks extends Idiot
{
  public function resolve(): self {
    // Ordenar por tiempo de sign up, de menor a mayor
    usort($this->libraries, function ($a, $b) {
      if ($a->totalBooks == $b->totalBooks) {
        return 0;
      }

      return ($a->totalBooks > $b->totalBooks) ? -1 : 1;
    });

    return $this;
  }
}
