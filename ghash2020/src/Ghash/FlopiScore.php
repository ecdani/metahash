<?php

namespace Ghash;

class FlopiScore extends Idiot
{
  public function resolve(): self {
    // Ordenar por tiempo de sign up, de menor a mayor
    usort($this->libraries, function ($a, $b) {
      if ($a->getBookScore() == $b->getBookScore()) {
        return 0;
      }

      return ($a->getBookScore() > $b->getBookScore()) ? -1 : 1;
    });

    return $this;
  }
}
