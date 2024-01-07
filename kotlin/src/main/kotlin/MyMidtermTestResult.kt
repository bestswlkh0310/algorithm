fun main() {
    val arr = arrayListOf<Double>()
    val subject = arrayListOf("영어", "국어", "수학", "사회", "과학")
    arr.add(97.0)
    arr.add(70.0)
    arr.add(100.0)
    arr.add(95.6)
    arr.add(95.5)
    for (i in arr.indices) {
        println("${subject[i]} : ${arr[i]}")
    }
    println("average : ${arr.average()}")
}