import kotlin.reflect.typeOf

fun main() {
    val num = readln().toInt()
    for (i in 1 .. num) {
        val inp = readln().split(" ").map { it.toInt() }
        var result = inp[0]
        for (j in 1 until inp[1]){
            result = (result * inp[0]) % 10
        }
        if (result == 0) {
            result = 10
        }
        println(result)
    }
}