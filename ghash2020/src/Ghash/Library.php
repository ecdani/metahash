<?php
namespace Ghash;

class Library {
  public $totalBooks;
  public $daysToSign;
  public $booksPerDay;
  public $books;
  public $id;
  public $bookTotalScore

  public function __construct($totalBooks, $daysToSign, $booksPerDay, $books, $id) {
    $this->totalBooks = $totalBooks;
    $this->daysToSign = $daysToSign;
    $this->booksPerDay = $booksPerDay;
    $this->books = $books;
    $this->id = $id;

    // echo "Total de libros: $this->totalBooks" . PHP_EOL;
    // echo "Días para firmar: $this->daysToSign" . PHP_EOL;
    // echo "Libros por día: $this->booksPerDay" . PHP_EOL;
    // echo "ID: $this->id" . PHP_EOL;
    // echo "Libros:" . PHP_EOL;
    // print_r($this->books);
  }

  public getBookScore() {
    return array_reduce(array_filter(Problem::bookScores, function(book, index) {
      return in_array(index, $this->books);
    } ), function(sum, a) {
      return sum + a;
    }, 0)
  }
}
// function que  calcule otra variable de la clase (bookScore)