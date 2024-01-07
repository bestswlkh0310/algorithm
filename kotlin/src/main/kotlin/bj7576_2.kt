import com.sun.org.apache.xpath.internal.operations.Bool
import java.util.*
import kotlin.math.max

fun main() {

    var queue: Queue<Pair<Int, Int>> = LinkedList()
    val (x, y) = readln().split(" ").map { it.toInt() }
    xPos = x
    yPos = y
    var arr: MutableList<MutableList<Int>> = arrayListOf()

    for (i in 0 until y) {
        arr.add(readln().split(" ").map { it.toInt() }.toMutableList())
        for (j in 0 until x) {
            if (arr[i][j] == 1) {
                queue.add(Pair(i, j))
            }
        }
    }

//    for (i in 0 .. 5) {
    while (!queue.isEmpty()) {
//        println(queue.element())

        val nowY = queue.peek().first
        val nowX = queue.peek().second
        queue.remove()

        for (i in weight) {
            val wY = nowY + i.first
            val wX = nowX + i.second
            if (isIn(wY, wX) && arr[wY][wX] == 0) {
                queue.add(Pair(wY, wX))
                arr[wY][wX] = arr[nowY][nowX] + 1
            }
        }
    }

    arr.forEach { if (it.contains(0)) return println(-1) }
    var mx = -2
    arr.forEach { it.forEach { mx = max(it, mx) } }
    println(mx - 1)
//    show(arr, y, x)

}

private var weight = arrayListOf(Pair(1,0),Pair(-1,0),Pair(0,1),Pair(0,-1))
private var xPos = 0
private var yPos = 0

private fun isIn(y: Int, x: Int): Boolean {
    return y in 0 until yPos && x in 0 until xPos
}

private fun show(arr: MutableList<MutableList<Int>>, y: Int, x: Int) {
    for (i in 0 until y) {
        for (j in 0 until x) {
            print("${arr[i][j]} ")
        }
        println()
    }
    println()
}