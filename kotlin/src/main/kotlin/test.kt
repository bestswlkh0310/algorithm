import java.lang.Exception

fun main() {
    val dog1 = Dog()
    val dog2 = Dog()

    dog1.damege()
    dog1.damege()

    println(dog2.hp)
}

class Dog {
    var hp = 10
    fun damege() {
        hp -= 4
    }

    fun berk() {
        println("월")
    }
}