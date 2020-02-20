<?php

namespace Ghash;

class Library {
  public $totalBooks;
  public $daysToSign;
  public $booksPerDay;
  public $books;
  public $id;

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
}
