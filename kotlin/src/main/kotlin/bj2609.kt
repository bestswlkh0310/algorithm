fun main() {
    val (a, b) = readln().split(" ").map { it.toInt() }
    println(gcd(a,b))
    println(a * b / gcd(a,b))
}

private fun gcd(a:Int,b:Int):Int = if(b!=0) gcd(b, a%b) else a