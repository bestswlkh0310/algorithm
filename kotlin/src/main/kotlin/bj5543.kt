fun main() {
    val bg = arrayListOf<Int>()
    val side = arrayListOf<Int>()
    val dd = arrayListOf<Int>()
    repeat(3) {
        bg.add(readln().toInt())
    }
    repeat(2) {
        side.add(readln().toInt())
    }
    println(bg.min() + side.min() - 50)
}