<?php

namespace Ghash;

class PruebaTonta extends Idiot {
  public function resolve(): self {
    $this->sortByBooksPerDay();
    $this->sortByBookScore();
    $this->sortByTotalBooks();
    $this->sortByDaysToSign();

    return $this;
  }

  public function sortByBookScore() {
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
  }

  public function sortByBooksPerDay() {
    usort($this->libraries, function ($a, $b) {
      if ($a->booksPerDay == $b->booksPerDay) {
        return 0;
      }

      return ($a->booksPerDay > $b->booksPerDay) ? -1 : 1;
    });
  }

  public function sortByTotalBooks() {
    // Ordenar por tiempo de sign up, de menor a mayor
    usort($this->libraries, function ($a, $b) {
      if ($a->totalBooks == $b->totalBooks) {
        return 0;
      }

      return ($a->totalBooks > $b->totalBooks) ? -1 : 1;
    });
  }

  public function sortByDaysToSign() {
    usort($this->libraries, function ($a, $b) {
      if ($a->daysToSign == $b->daysToSign) {
        return 0;
      }

      return ($a->daysToSign < $b->daysToSign) ? -1 : 1;
    });

    return $this;
  }
}
