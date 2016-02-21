import Control.Applicative(Applicative(..),ZipList(..),(<$>))
import Data.List(sortBy, intersperse, and, elemIndex, nub, group, sort)
import Data.Maybe(fromJust)

data Warehouse = WH {
	getXWH, getYWH :: Int,
	getItemsWH :: [Int]
} deriving (Eq, Show)

data Order = Order {
	getXO, getYO, getProducts :: Int,
	getItemsO :: [Int]
} deriving (Eq, Show)

data Data = Data {
	getRows, getColumns, getNDrones, getTurns, getMaxW, getTypeP, getWarehouseLength, getOrdersLength :: Int,
	getWeight :: [Int],
	getWarehouse :: [Warehouse],
	getOrders :: [Order],
	getDrones :: [Drone]
} deriving (Eq, Show)

data Command = L Int Int Int Int | U Int Int Int Int | D Int Int Int Int | W Int Int

type Row = Int
type Column = Int
type Product = Int
type Weight = Int
type Drone = (Bool, (Row,Column), [Product])

instance Show Command where
	show (L x y z w) = (show x) ++ "L" ++ (show y) ++ (show z) ++ (show w)
	show (U x y z w) = (show x) ++ "U" ++ (show y) ++ (show z) ++ (show w)
	show (D x y z w) = (show x) ++ "D" ++ (show y) ++ (show z) ++ (show w)
	show (W x y) = (show x) ++ "W" ++ (show y)

main = do
	file <- getContents
	let
		d = readData $ lines file
		o = orderByEasy d
		s = solve o 0
	putStrLn $ concat (intersperse "\n" (map show s))

readData :: [String] -> Data
readData (x:y:z:w:xs) = Data h1 h2 h3 h4 h5 tp wl ol aw gw go dr
	where
		(h1:h2:h3:h4:h5:[]) = map read (words x) :: [Int]
		tp = read y :: Int
		aw = map read (words z) :: [Int]
		wl = read w :: Int
		ol = read $ xs !! (wl * 2) :: Int
		gw = readWarehouses $ take (wl * 2) xs
		go = readOrders $ drop (ol * 3) xs
		wlf = head gw
		dr = take h3 $ repeat (False, (getXWH wlf, getYWH wlf), [])

readWarehouses :: [String] -> [Warehouse]
readWarehouses [] = []
readWarehouses x = (WH (a !! 0) (a !! 1) it) : readWarehouses (tail $ tail x)
	where
		a = map read (words $ head x) :: [Int]
		it = map read (words (x !! 1)) :: [Int]

readOrders :: [String] -> [Order]
readOrders [] = []
readOrders x = (Order (a !! 0) (a !! 1) cp tp) : readOrders (tail $ tail $ tail x)
	where
		a = map read (words $ head x) :: [Int]
		cp = read (x !! 1) :: Int
		tp = map read (words (x !! 2)) :: [Int]

applyCommand :: Data -> Command -> Data
applyCommand d cmd = d

orderByEasy :: Data -> Data
orderByEasy (Data h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12) = (Data h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 (orderOrder h11) h12)
	
orderOrder :: [Order] -> [Order]
orderOrder = sortBy (\x y -> compare (getProducts x) (getProducts y))

getWarehouseByProduct :: Data -> Product -> Int -> Warehouse
getWarehouseByProduct d p t = head [x | x <- getWarehouse d, (getItemsWH x !! p) >= t]

getFreeDrone :: Data ->  Maybe Int
getFreeDrone d = getFreeDrone' d 0

getFreeDrone' :: Data -> Int -> Maybe Int
getFreeDrone' d i = if i < (getNDrones d) then (if isFreeDrone ((getDrones d) !! i) then Just i else getFreeDrone' d (i+1)) else Nothing
		
isFreeDrone :: Drone -> Bool
isFreeDrone (x,y,z) = not x

removeOrder :: Data -> Data
removeOrder (Data h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12) = (Data h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 (tail h11) h12)

firstOrder :: Data -> Order
firstOrder d = head $ getOrders d

foldOrder :: Order -> [(Product, Int)]
foldOrder o = map (\x -> (head x, length x)) . group . sort $ getItemsO o

solve :: Data -> Int -> [Command]
solve d x = if x >= getTurns d then [] else (L 0 0 0 0) : solve d' 0
	where
		fdrone = getFreeDrone d
		xx = if fdrone == Nothing then x+1 else x
		forder = firstOrder d
		items = foldOrder forder
		w = map (\i -> getWarehouseByProduct d (fst i) (snd i)) items
		d' = removeOrder d
	
	
	
