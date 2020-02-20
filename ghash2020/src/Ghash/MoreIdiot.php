<?php

namespace Ghash;

class MoreIdiot extends Idiot
{
  public function resolve(): self {
    // Ordenar por tiempo de sign up, de menor a mayor
    usort($this->libraries, function ($a, $b) {
      if ($a->daysToSign == $b->daysToSign) {
        return 0;
      }

      return ($a->daysToSign < $b->daysToSign) ? -1 : 1;
    });

    return $this;
  }
}
