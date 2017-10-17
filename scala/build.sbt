lazy val sparkVersion = "2.0.0"
val framelessVersion = "0.3.0"

organization := "com.github.shokohara"
scalaVersion := "2.11.8"
name := "titanic"
libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % sparkVersion,
  "org.apache.spark" %% "spark-sql" % sparkVersion,
  "org.apache.spark" %% "spark-streaming" % sparkVersion,
  "org.apache.spark" %% "spark-mllib" % sparkVersion,
  "org.apache.spark" %% "spark-hive" % sparkVersion,
  "org.apache.spark" %% "spark-tags" % sparkVersion,
  "org.apache.spark" %% "spark-mllib-local" % sparkVersion,
  "org.apache.spark" %% "spark-network-common" % sparkVersion,
  "org.apache.spark" %% "spark-graphx" % sparkVersion,
  "org.apache.spark" %% "spark-catalyst" % sparkVersion,
  "org.typelevel" %% "frameless-cats" % framelessVersion,
  "org.typelevel" %% "frameless-dataset" % framelessVersion
)
mainClass := Option("com.github.shokohara.titanic.Main")
