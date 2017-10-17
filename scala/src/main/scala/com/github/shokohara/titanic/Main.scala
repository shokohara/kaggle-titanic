package com.github.shokohara.titanic

import org.apache.spark.SparkConf
import org.apache.spark.ml.feature.StopWordsRemover
import org.apache.spark.sql.{DataFrame, Row, SparkSession}

object Main {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf()
      .setMaster("local[*]")
    //      .setAppName("my app")
    //      .set("spark.executor.memory", "1g")
    val spark: SparkSession = SparkSession.builder
      .config(conf)
      .appName("spark session example")
      .getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")
    import org.apache.spark.sql.functions._
    val logData: DataFrame = spark.read
      .format("csv")
      .option("header", "true")
      .option("inferSchema", "true")
      .load("train.csv")
      .transform(df => df.withColumn("AltSex", col("Sex")))
    logData.show
    //    val numAs = logData.filter(line => line.contains("a")).count()
    //    val numBs = logData.filter(line => line.contains("b")).count()
    //    println(s"Lines with a: $numAs, Lines with b: $numBs")
    spark.stop()
  }
}
