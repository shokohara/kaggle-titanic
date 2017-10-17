package com.github.shokohara.titanic

import org.apache.spark.SparkConf
import org.apache.spark.sql.{SQLContext, SparkSession}
import org.apache.log4j.{Level, Logger}
object Main {
  case class MyData(PassengerId: Int,
                    Survived: Int,
                    Pclass: Int,
                    Name: String,
                    Sex: String,
                    Age: Double,
                    SibSp: Int,
                    Parch: Int,
                    Ticket: String,
                    Fare: Double,
                    Cabin: String,
                    Embarked: String)
  def main(args: Array[String]): Unit = {
    Logger.getRootLogger.setLevel(Level.WARN)
    val conf = new SparkConf()
      .setMaster("local[*]")
    //      .setAppName("my app")
    //      .set("spark.executor.memory", "1g")
    val spark: SparkSession = SparkSession.builder
      .config(conf)
      .appName("spark session example")
      .getOrCreate()
    spark.sparkContext.setLogLevel("OFF")
    import spark.sqlContext.implicits._
    println {
      spark.read
        .format("csv")
        .option("header", "true")
        .option("inferSchema", "true")
        .load("train.csv")
//      .printSchema()
        .rdd
        .map { r =>
          MyData(
            PassengerId = r.getAs("PassengerId"),
            Survived = r.getAs("Survived"),
            Pclass = r.getAs("Pclass"),
            Name = r.getAs("Name"),
            Sex = r.getAs("Sex"),
            Age = r.getAs("Age"),
            SibSp = r.getAs("SibSp"),
            Parch = r.getAs("Parch"),
            Ticket = r.getAs("Ticket"),
            Fare = r.getAs("Fare"),
            Cabin = r.getAs("Cabin"),
            Embarked = r.getAs("Embarked")
          )
        }
        .toDF()
        .createOrReplaceTempView("temp")
      spark.sqlContext.sql("select PassengerId from temp").show()
//        .printSchema()
//        .show(10000)
    }
    spark.stop()
  }
}
//      .transform(df => df.withColumn("AltSex", col("Sex")))
//      .map { row: Row =>
//        (1, 2)
//        row
//      }

//    val numAs = logData.filter(line => line.contains("a")).count()
//    val numBs = logData.filter(line => line.contains("b")).count()
//    println(s"Lines with a: $numAs, Lines with b: $numBs")
