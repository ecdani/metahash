<?php
namespace Ghash;

class Library {
  public $totalBooks;
  public $daysToSign;
  public $booksPerDay;
  public $books;
  public $id;
  public $bookTotalScore;
  public $totalScore;
  public $bookScores;

  public function __construct($totalBooks, $daysToSign, $booksPerDay, $books, $id, $bookScores) {
    $this->totalBooks = $totalBooks;
    $this->daysToSign = $daysToSign;
    $this->booksPerDay = $booksPerDay;
    $this->books = $books;
    $this->id = $id;
    $this->bookScores = $bookScores;

    // echo "Total de libros: $this->totalBooks" . PHP_EOL;
    // echo "Días para firmar: $this->daysToSign" . PHP_EOL;
    // echo "Libros por día: $this->booksPerDay" . PHP_EOL;
    // echo "ID: $this->id" . PHP_EOL;
    // echo "Libros:" . PHP_EOL;
    // print_r($this->books);
  }

  public function getBookScore() {
    return array_reduce(array_filter($this->bookScores, function($book, $index) {
      return in_array($index, $this->books);
      }), function($sum, $a) {
        return $sum + $a;
      }, 0);
  }
}
// function que  calcule otra variable de la clase (bookScore)