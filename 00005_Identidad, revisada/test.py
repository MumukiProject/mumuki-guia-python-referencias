def test_"referencias_repetidas es una lista":
  expect(referencias_repetidas.is_a? Array).to be True


def test_"referencias_repetidas tiene tres elementos":
  expect(referencias_repetidas.size).to eq 3


def test_"Todos los objetos de referencias_repetidas son el mismo":
  expect(referencias_repetidas.all? { |referencia| referencia.equal? referencias_repetidas.first }).to be True
