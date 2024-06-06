# Characters (Presentation Layer)

## Definition
In the context of the Presentation Layer, characters refer to the character sets and encoding schemes used to represent data. This layer ensures that data is in a usable format and is where data encryption occurs.

## Character Sets and Encoding
1. **ASCII (American Standard Code for Information Interchange):** A character encoding standard used to represent text in computers and other devices that use text. ASCII codes represent text in computers, telecommunications equipment, and other devices.
2. **Unicode:** A computing industry standard for the consistent encoding, representation, and handling of text expressed in most of the world's writing systems. It includes nearly all scripts (alphabets), and is the basis for most modern character encodings.
3. **UTF-8:** A variable-width character encoding capable of encoding all 1,112,064 valid character code points in Unicode using one to four 8-bit bytes. It's the dominant character encoding for the World Wide Web.

## Role of Characters in the Presentation Layer
The Presentation Layer is responsible for the delivery and formatting of information to the Application Layer for further processing or display. It relieves the Application Layer of concern regarding syntactical differences in data representation within the end-user systems. In the context of characters, the Presentation Layer ensures that text data is correctly encoded and decoded using the appropriate character sets.

#### Key Insights

- Character encoding is crucial for transmitting and decoding data across computer networks.
- ASCII and ISO 8859 are two widely used character encoding standards.
- The presentation layer plays a vital role in ensuring compatibility and understanding between different machines.
- The inclusion of control characters in ASCII helps with data delineation and communication in network protocols.
- ISO 8859 extended ASCII to include additional characters for various languages, improving international compatibility.