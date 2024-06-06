# Universal Characters (Presentation Layer)

## Definition
Universal characters refer to the universal character set (UCS), a standard set of characters used by many of the world's writing systems. The most commonly used form of the UCS is Unicode.

## Unicode
Unicode is a computing industry standard designed to consistently and uniquely encode characters used in written languages, and used for text representation in the digital world. It includes characters from almost all scripts (alphabets) around the world, as well as many special characters.

## UTF-8, UTF-16, and UTF-32
These are different encodings used to represent Unicode characters as digital data. UTF-8 uses 1-4 bytes per character, UTF-16 uses 2 or 4 bytes, and UTF-32 uses 4 bytes for each character.

## Role of Universal Characters in the Presentation Layer
The Presentation Layer is responsible for the delivery and formatting of information to the Application Layer for further processing or display. It ensures that data is in a usable format and is where data encryption occurs. In the context of universal characters, the Presentation Layer ensures that text data is correctly encoded and decoded using the appropriate Unicode encoding. This allows for the accurate and consistent representation of text in any language.

#### Key Insights

- Unicode was developed to solve the limitation of early codes in transmitting universal characters, representing all languages and even characters from extinct alphabets.
- The Unicode codepoint for a character can be represented in UTF-8 using a variable length representation, with shorter sequences for commonly used characters and longer sequences for less common ones.
- The encoding scheme of UTF-8 uses specific patterns in the leading bits of each byte to indicate the length of the character sequence, allowing efficient representation of characters.
- UTF-8 is widely used due to its compatibility with ASCII, efficient representation of commonly used characters, and support for a wide range of characters from different languages.
- Other encoding schemes like UTF-16 and UTF-32 exist, but UTF-8 is the most popular due to its efficiency and compatibility with existing systems.