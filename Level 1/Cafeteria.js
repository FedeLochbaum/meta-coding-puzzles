const get_seats_in_range = (I, E, K) =>
  E < I ? 0 : E === I ? 1 : Math.ceil((E - I + 1) / (K + 1))

const getMaxAdditionalDinersCount = (N, K, M, S) => {
  const sorted = S.sort((a, b) => a - b)

  let max = get_seats_in_range(1, sorted[0] - (K + 1), K)

  for (let i = 0; i < sorted.length - 1; i++) {
    max += get_seats_in_range(sorted[i] + K + 1, sorted[i + 1] - (K + 1), K)
  }

  return max + get_seats_in_range(sorted[sorted.length - 1] + K + 1, N, K)
}