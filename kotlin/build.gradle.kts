plugins {
    kotlin("jvm") version "1.9.20"
    application
}

group = "io.github.icebreaking310"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
}

dependencies {
    testImplementation(kotlin("test"))
}

tasks.test {
    useJUnitPlatform()
}

application {
    mainClass.set("MainKt")
}