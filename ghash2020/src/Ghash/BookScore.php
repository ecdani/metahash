<?php

namespace Ghash;

class BookScore extends Idiot
{
  public function resolve(): self {
    foreach ($this->libraries as $key => $library) {
      $this->libraries[$key]->totalScore = array_reduce($library->books, function ($sum, $bookKey) use ($library) {
        return $sum + $library->bookScores[$bookKey];
      }, 0);
    }
    usort($this->libraries, function ($a, $b) {
      if ($a->totalScore == $b->totalScore) {
        return 0;
      }

      return ($a->totalScore > $b->totalScore) ? -1 : 1;
    });

    return $this;
  }
}
