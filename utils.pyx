cpdef chunk_write(str output_path, list data):
    with open(output_path, "a") as f:
        for i in data:
            f.write(f"{i}\n")

cpdef generate_id(int gender, str city, int city_code, str output_path):
    cdef str prefix = city.upper() + str(gender)
    cdef str id_number = ""
    cdef list data = []
    cdef int chunk_size = 1000000

    with open(output_path, "a") as f:
        for i in range(100000000):
            id_number = prefix + str(i).zfill(8)
            if validate_id(id_number, city_code):
                data.append(id_number)
            if len(data) == chunk_size:
                chunk_write(output_path, data)
                data = []


cpdef validate_id(str id_number, int city_code):
    cdef list be_multiplied = [city_code // 10, city_code % 10]
    cdef list to_be_extended = [int(i) for i in id_number[1:]]
    be_multiplied.extend(to_be_extended)
    cdef list to_multiply = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
    cdef int _sum = sum([be_multiplied[i] * to_multiply[i] for i in range(len(be_multiplied))])
    return _sum % 10 == 0