import kotlin.math.*

fun main() {
    var (day, start) = readln().split(" ").map { it.toInt() }
    var h = ceil((start + day - 1) / 7.0).toInt()
    println(h)

    println("+–––––––––––––––––––––+")
    var sum = 1
    for (i in 1 .. h) {
        print("|")
        for (j in 1 .. 7) {
            if (sum < start) {
                print("...")
                sum++
                continue
            }
            if ((i - 1) * 7 + j - start < day) {
                print("${((i - 1) * 7 + j + 1 - start).toString().padStart(3, '.')}")
            } else {
                print("...")
            }
        }
        println("|")
    }
    println("+---------------------+")
}