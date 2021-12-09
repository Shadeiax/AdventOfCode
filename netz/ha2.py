import collections
import random
import statistics

import numpy
from matplotlib import pyplot as plt

# CONFIG & DATA CLASSES #
SOURCES = 3
PACKET_MIN_SIZE = 64
PACKET_MAX_SIZE = 1500
PACKETS_PER_SOURCE = 10000000
# bytes/s
TRANSFER_SPEED = 1.0

# IMPLEMENTATION #
# contains a queue for each source, which each contain the respective packet sizes in bytes (int representation)
sources = [[] for _ in range(SOURCES)]


def generate_packets():
    for source_idx in range(SOURCES):
        for packet_idx in range(PACKETS_PER_SOURCE):
            packet_size = random.randint(PACKET_MIN_SIZE, PACKET_MAX_SIZE)
            sources[source_idx].append(packet_size)


def add_measurement(time_per_size, packet_size, transfer_time):
    if packet_size not in time_per_size:
        time_per_size[packet_size] = []
    time_per_size[packet_size].append(transfer_time)


def process_queue_rr():
    # packet size (int) -> array of total transfer times (float)
    time_per_size = {}
    # in seconds
    passed_time = 0

    empty_sources = [[] for _ in range(SOURCES)]
    while sources != empty_sources:
        for source_idx in range(SOURCES):
            if len(sources[source_idx]) == 0:
                continue
            packet_size = sources[source_idx].pop()
            passed_time += packet_size / TRANSFER_SPEED
            add_measurement(time_per_size, packet_size, passed_time)
    return time_per_size


def process_queue_fq():
    # packet size (int) -> array of total transfer times (float)
    time_per_size = {}
    # in seconds
    passed_time = 0

    prev_finish_times = [0 for _ in range(SOURCES)]
    empty_sources = [[] for _ in range(SOURCES)]
    while sources != empty_sources:
        # calculate which packet would theoretically finish first
        min_source_idx = -1
        min_finish_time = -1
        for source_idx in range(SOURCES):
            if len(sources[source_idx]) == 0:
                continue
            packet_size = sources[source_idx][-1]
            finish_time = prev_finish_times[source_idx] + (packet_size/TRANSFER_SPEED)
            if min_finish_time == -1 or finish_time < min_finish_time:
                min_source_idx = source_idx
                min_finish_time = finish_time

        # send respective packet
        packet_size = sources[min_source_idx].pop()
        passed_time += packet_size / TRANSFER_SPEED
        add_measurement(time_per_size, packet_size, passed_time)

        # update previous finish times
        prev_finish_times[min_source_idx] = passed_time
    return time_per_size


def draw_plot(axes, mode, value_dict):
    value_dict = collections.OrderedDict(sorted(value_dict.items()))
    x = list(value_dict.keys())
    y = [statistics.fmean(measurements) for measurements in value_dict.values()]
    axes.plot(x, y)

    # draw trend line
    z = numpy.polyfit(x, y, 1)
    p = numpy.poly1d(z)
    axes.plot(x, p(x), "r--")

    # add metadata
    axes.set_xlabel("Packet size (bytes)")
    axes.set_ylabel("Transfer time (seconds)")
    axes.set_title(mode)


def main():
    # create general figure
    fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)
    fig.suptitle(f"Transfer speed {TRANSFER_SPEED} bytes/s | {SOURCES} sources | {PACKETS_PER_SOURCE} packets/source"
                 f"\nArrival time equal for every packet")

    # execute round robin queue and draw respective subplot
    generate_packets()
    time_per_size = process_queue_rr()
    draw_plot(axs[0], "Round Robin", time_per_size)

    # execute fair queuing queue and draw respective subplot
    generate_packets()
    time_per_size = process_queue_fq()
    draw_plot(axs[1], "Fair Queuing", time_per_size)

    fig.tight_layout()
    fig.show()


if __name__ == '__main__':
    main()