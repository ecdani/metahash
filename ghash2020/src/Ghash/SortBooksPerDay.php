<?php

namespace Ghash;

class SortBooksPerDay extends Idiot
{
  public function resolve(): self {
    usort($this->libraries, function ($a, $b) {
      if ($a->booksPerDay == $b->booksPerDay) {
        return 0;
      }

      return ($a->booksPerDay > $b->booksPerDay) ? -1 : 1;
    });

    return $this;
  }
}
