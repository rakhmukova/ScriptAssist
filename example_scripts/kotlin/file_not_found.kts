import java.io.File
import java.io.FileReader

val file = File("path/to/nonexistent_file.txt")
val reader = FileReader(file)
reader.read()
reader.close()