# Hamming Code (Data Link Layer)

## Definition
Hamming code is an error-detection and error-correction method used in data communication. It employs parity bits to detect and correct single-bit errors in transmitted data, ensuring higher data integrity and reliability.

## How it Works
### 1. Parity Bits
- **Function:** Parity bits are added to the data to protect a specific set of bits. The position and value of these parity bits are determined based on the data bits.
- **Example:** For a 4-bit data word (d1, d2, d3, d4), three parity bits (p1, p2, p4) are added, resulting in a 7-bit code word (p1, p2, d1, p4, d2, d3, d4).

### 2. Even Parity
- **Definition:** Even parity means that the total number of 1's in a set (including the parity bit) should be even.
- **Example:** If the data bits are 1010 and even parity is used, the parity bits are set to ensure the total number of 1's (data bits + parity bit) in each set is even.

### 3. Error Correction
- **Detection:** If a bit is received incorrectly (e.g., flipped from 1 to 0), the parity bits can identify the erroneous bit.
- **Correction:** By analyzing the positions of the parity bits and their values, the exact bit that has changed can be pinpointed and corrected.

## Hamming Code Structure
### 1. Single Bit Error Correction
- **Mechanism:** Basic Hamming code can correct single-bit errors by placing each data bit in multiple sets, each protected by a parity bit.
- **Example:** For a 4-bit data word, the parity bits are calculated and placed at positions that are powers of two (1, 2, 4), resulting in a 7-bit code word.

### 2. Multiple Bit Error Correction
- **Extended Hamming Code:** To correct multiple bit errors, the Hamming code can be extended by adding more parity bits.
- **Example:** Adding an overall parity bit to the existing Hamming code can help detect double-bit errors, though correction is typically limited to single-bit errors.

## Role of Hamming Code in the Data Link Layer
The Data Link Layer is responsible for error detection and correction in data transmission. Hamming code is one method it uses to achieve this, ensuring that data is transmitted accurately and reliably.

### Key Insights
- **Protecting Specific Bits:** Hamming codes use parity bits to protect specific sets of bits, allowing the identification of which bit has changed during transmission errors.
- **Single Bit Error Correction:** The mechanism to correct a single-bit error involves using parity bits and intersections of sets to identify the incorrect bit.
- **Binary Counting:** Binary counting is used to indicate the combinations of sets and intersections in Hamming codes, helping in the calculation of parity bits.
- **Bit Sequence:** Hamming codes require calculating and transmitting both parity and data bits in a specific sequence to ensure accurate detection and correction.
- **Error Correction Process:** The error correction process involves checking the received bit string, using the calculated parity bits to identify and correct the error.
- **Limitations:** Hamming codes are limited in their ability to correct multiple bit errors, and the presence of damaged parity bits can impact error correction capabilities.

### Example of Hamming Code
Let's illustrate with an example to show how Hamming code detects and corrects errors.

#### 1. Encoding
Suppose we have a 4-bit data word: `1010`.

- Position the data bits with placeholder parity bits:
  ```
  p1 p2 d1 p4 d2 d3 d4
  _  _  1  _  0  1  0
  ```
- Calculate the parity bits:
  - `p1` covers bits 1, 3, 5, 7 → `p1` = parity of (1, 0, 0) = 1 (even parity)
  - `p2` covers bits 2, 3, 6, 7 → `p2` = parity of (1, 1, 0) = 0 (even parity)
  - `p4` covers bits 4, 5, 6, 7 → `p4` = parity of (0, 1, 0) = 1 (even parity)

  Resulting in:
  ```
  p1 p2 d1 p4 d2 d3 d4
  1  0  1  1  0  1  0
  ```

#### 2. Transmission
The transmitted 7-bit code is: `1011010`.

#### 3. Error Detection and Correction
Assume an error occurs, and the received code is: `1111010`.

- Calculate the parity check bits:
  - Check `p1` for bits 1, 3, 5, 7 → expected parity = 1, actual = 1 (match)
  - Check `p2` for bits 2, 3, 6, 7 → expected parity = 0, actual = 1 (mismatch)
  - Check `p4` for bits 4, 5, 6, 7 → expected parity = 1, actual = 1 (match)

  Parity mismatches indicate bit 2 is erroneous. 

- Correct the error by flipping bit 2:
  - Received: `1111010`
  - Corrected: `1011010`

The corrected code matches the originally transmitted code, ensuring data integrity.