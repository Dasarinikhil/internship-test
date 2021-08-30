import pandas as pd
def get2Smallest(arr):
    arr_size = len(arr)
    if arr_size < 2:
        return arr[0],None;
    first = second = 1000000007
    for i in range(0, arr_size):
        if arr[i] < first:
            second = first
            first = arr[i]
        elif (arr[i] < second and arr[i] != first):
            second = arr[i]
    return first,second

if __name__ == "__main__":
  df = pd.read_csv("filteredCountry.csv")
  SKU = []
  firstMin = []
  secondMin = []
  for each in df.SKU.unique():
    pricedf = df[df['SKU']==each]
    prices = pricedf.PRICE.unique()
    arr = []
    for val in prices:
      val = val.replace('$','')
      val = val.replace(',','')
      val = val.replace('?','')
      arr.append(float(val))

    first, second = get2Smallest(arr)
    if first is None or second is None:
      continue
    else:
      if first.is_integer():
        first = int(first)
      if second.is_integer():
        second = int(second)
      SKU.append(each)
      firstMin.append(str(first))
      secondMin.append(str(second))

  result = pd.DataFrame({'SKU':SKU,'FIRST_MINIMUM_PRICE':firstMin,'SECOND_MINIMUM_PRICE':secondMin})
  result.to_csv("lowestPrice.csv",index=False)