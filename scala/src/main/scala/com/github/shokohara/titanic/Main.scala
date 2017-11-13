package com.github.shokohara.titanic

import java.io.File

import breeze.linalg._
import breeze.numerics._
import breeze.io.CSVReader._
import better.files._

object Main {
  def main(args: Array[String]): Unit = {
    println(file"train.csv".toJava.getAbsolutePath)
    val csv: DenseMatrix[Double] = csvread(file"train.csv".toJava)
    read(file"train.csv".newFileReader)
//    println(csv)
  }
}
