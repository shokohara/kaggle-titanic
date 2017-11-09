lazy val breezeVersion = "0.13.2"

lazy val root = project

organization := "com.github.shokohara"
scalaVersion := "2.11.8"
name := "titanic"
resolvers ++= Seq(
  "Sonatype Snapshots" at "http://oss.sonatype.org/content/repositories/snapshots",
  "Sonatype Releases" at "http://oss.sonatype.org/content/repositories/releases"
)

libraryDependencies ++= Seq(
  "org.scala-saddle" %% "saddle-core" % "1.3.+",
  "com.github.pathikrit" %% "better-files" % "2.17.1",
  "org.scalanlp" %% "breeze" % breezeVersion,
  "org.scalanlp" %% "breeze-natives" % breezeVersion,
  "org.scalanlp" %% "breeze-viz" % breezeVersion
//  "org.apache.spark" %% "spark-core" % sparkVersion,
//  "org.apache.spark" %% "spark-sql" % sparkVersion,
//  "org.apache.spark" %% "spark-streaming" % sparkVersion,
//  "org.apache.spark" %% "spark-mllib" % sparkVersion,
//  "org.apache.spark" %% "spark-hive" % sparkVersion,
//  "org.apache.spark" %% "spark-tags" % sparkVersion,
//  "org.apache.spark" %% "spark-mllib-local" % sparkVersion,
//  "org.apache.spark" %% "spark-network-common" % sparkVersion,
//  "org.apache.spark" %% "spark-graphx" % sparkVersion,
//  "org.apache.spark" %% "spark-catalyst" % sparkVersion,
//  "org.typelevel" %% "frameless-cats" % framelessVersion,
//  "org.typelevel" %% "frameless-dataset" % framelessVersion
)
mainClass := Option("com.github.shokohara.titanic.Main")
