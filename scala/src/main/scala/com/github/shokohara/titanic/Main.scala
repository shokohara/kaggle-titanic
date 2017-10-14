package com.github.shokohara.titanic

import org.apache.spark.SparkConf
import org.apache.spark.sql.{DataFrame, SparkSession}

object Main {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf()
      .setMaster("local[*]")
    //      .setAppName("my app")
    //      .set("spark.executor.memory", "1g")
    val spark: SparkSession = SparkSession.builder.config(conf).appName("spark session example")
      .getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")
    val logData: DataFrame = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("train.csv")
      val x: DataFrame = logData.map(_.getAs[])
    //    logData.show
    //    val numAs = logData.filter(line => line.contains("a")).count()
    //    val numBs = logData.filter(line => line.contains("b")).count()
    //    println(s"Lines with a: $numAs, Lines with b: $numBs")
    spark.stop()
  }
}
