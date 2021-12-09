def is_parity(index):
    return ((index - 1) & index) == 0


def encode(input):
    output = [0] * 11
    written = 0

    for i in range(1, 12):
        if not is_parity(i):
            # Take value from input array, which will be written to
            # the output directly and added to the parity bits.
            value = input[written]

            for k in range(0, 4):
                # Iterate over bit sequence of this index and add the
                # previously taken value to the parity bits described
                # in this sequence ("one"-bits).
                masked = i & (1 << k)
                if masked > 0:
                    output[masked - 1] += value

            # Write value itself to output
            output[i - 1] = value
            written += 1

    # Modulo on parity bits, since they currently
    # contain the accumulated values of the bits that
    # are watched by it.
    for i in range(0, 4):
        print("Index: ", 2 ** i, " , ", output[2 ** i])
        output[(2 ** i) - 1] %= 2

    return output


def decode(input):
    output = [0] * 7
    parities = [0] * 4

    # First, all parity are recalculated the parities, so
    # that erroneous bits in the sequence can be pin-pointed
    # by comparing these results with what information the
    # given parity bits carry.
    for i in range(1, 12):
        if not is_parity(i):

            # The "one"-bits in the "Hamming Positions" (one-based) define,
            # which the corresponding parity bits for these fields are.
            # The value of the inspected field is added to all detected
            # parity fields; so the ones, whose respective bit is a one
            # in the binary sequence of the inspected fields position.
            value = input[i - 1]
            for k in range(0, 4):
                masked = (i >> k) & 1
                if masked:
                    parities[k] += value

    # Each newly calculated parity bit is compared with the one
    # in the input sequence. If they don't match, the position of
    # the mismatched parity bit in the "Hamming Code" is added to
    # an accumulator, which then represents the flipped field.
    error = 0
    pos = 1
    for i in range(0, 4):
        # The new parities might be accumulated, which is why
        # they modulo must be applied to normalize the values.
        if parities[i] % 2 != input[pos - 1]:
            error += pos

        pos <<= 1

    # The real data is extracted by iterating over the incoming
    # "Hamming Code". If the erroneous index is traversed, its
    # flipped value is stored in the output sequence.
    read = 0
    for i in range(1, 12):
        if not is_parity(i):
            value = input[i - 1]
            if i != error:
                output[read] = value
            else:
                output[read] = ~value & 1
            read += 1

    return output


def main():
    input = [0, 1, 1, 0, 0, 0, 1]
    encoded = encode(input)

    print("_ ", end='')
    for i in range(0, len(encoded)):
        print(encoded[i], end=' ')
        if (i + 2) % 4 == 0:
            print()

    decoded = decode(encoded)
    for i in range(0, len(decoded)):
        print(decoded[i], end='')
        if i < len(decoded) - 1:
            print(", ", end='')

    return


if __name__ == '__main__':
    main()