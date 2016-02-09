import Control.Applicative(Applicative(..),ZipList(..),(<$>))
import Data.List(sortBy, intersperse, and)

data Paint = Paint {
	getRows, getColumns :: Int,
	getLines, getFill :: [[Bool]]
} deriving (Read, Show)

data Command = PAINT_SQUARE Int Int Int | PAINT_LINE Int Int Int Int | ERASE_CELL Int Int deriving (Show)
type Row = Int
type Column = Int

main = do
	file <- getContents
	let
		p = getPaint $ lines file
		s = solve p
		h = (show $ length s) ++ "\n"
		t = concat (intersperse "\n" (map show s))
	putStrLn (h ++ t)

getPaint :: [String] -> Paint
getPaint content = Paint rows cols lines fill
	where
		f = map (=='#')
		first_line = words $ head content
		rows = read $ first_line !! 0 :: Int
		cols = read $ first_line !! 1 :: Int
		lines = map f $ tail content
		fill = take rows $ repeat (take cols (repeat False))

getPoint :: Paint -> Row -> Column -> Bool
getPoint p x y = x >= 0 && y >= 0 && x < (getRows p) && x < (getColumns p) && getLines p !! x !! y

getOneFill :: Paint -> Row -> Column -> Bool
getOneFill p x y = x >= 0 && y >= 0 && x < (getRows p) && x < (getColumns p) && getFill p !! x !! y

getAllCommands :: Paint -> [Command]
getAllCommands p = allRows ++ allCols
	where
		allRows = concat $ map (\x -> getAllHorizontal p x 0 (getColumns p - 1)) [0..(getRows p - 1)]
		allCols = concat $ map (\x -> getAllVertical p x 0 (getRows p - 1)) [0..(getColumns p - 1)]

getAllHorizontal :: Paint -> Row -> Column -> Column -> [Command]
getAllHorizontal p r c1 c2
	| c1 > (getColumns p - 1) = []
	| validCommand p l = l : getAllHorizontal p r (c2 + 2) (getColumns p - 1)
	| getPoint p r c1 = getAllHorizontal p r c1 (c2 - 1)
	| getPoint p r c2 = getAllHorizontal p r (c1 + 1) c2
	| otherwise = getAllHorizontal p r (c1 + 1) (c2 - 1)
		where
			l = PAINT_LINE r c1 r c2
			
getAllVertical :: Paint -> Column -> Row ->  Row -> [Command]
getAllVertical p c r1 r2
	| r1 > (getRows p - 1) = []
	| r1 > r2 = getAllVertical p c (r2 + 1) (getRows p - 1)
	| validCommand p l = l : getAllVertical p c (r2 + 2) (getRows p - 1)
	| getPoint p r1 c = getAllVertical p c r1 (r2 - 1)
	| getPoint p r2 c = getAllVertical p c (r1 + 1) r2
	| otherwise = getAllVertical p c (r1 + 1) (r2 - 1)
		where
			l = PAINT_LINE r1 c r2 c

validCommand :: Paint -> Command -> Bool
validCommand p cmd = and (map (\(a,b) -> getPoint p a b) (getTuples cmd))

lengthCommand :: Command -> Int
lengthCommand (PAINT_LINE r1 c1 r2 c2) = max (r1 - r2) (c1 - c2)
lengthCommand (PAINT_SQUARE r c s) = (2 * s + 1) * (2 * s + 1)

diffCommand :: Paint -> Command -> Int
diffCommand p cmd = length $ filter (==False) (map (\(a,b) -> getOneFill p a b) t)
	where
		t = getTuples cmd

getReadyCommands :: Paint -> [Command]
getReadyCommands p = getOrderedCommands p (getAllCommands p)

getOrderedCommands :: Paint -> [Command] -> [Command]
getOrderedCommands p@(Paint _ _ _ f) x = sortBy (\a b -> compare (diffCommand p b) (diffCommand p a)) x

applyCommand :: Paint -> Command -> Paint
applyCommand (Paint r c l f) cmd = Paint r c l (maskCommand f cmd)

maskCommand :: [[Bool]] -> Command -> [[Bool]]
maskCommand m cmd = foldl (\acc (x,y) -> (take (x) acc) ++ (take (y) (acc !! x) ++ True : (drop (y+1) (acc !! x))) : (drop (x+1) acc)) m t
	where
		t = getTuples cmd

getTuples :: Command -> [(Int,Int)]
getTuples (PAINT_LINE r1 c1 r2 c2)
	| r1 == r2 = map (\x -> (r1,x)) [c1..c2]
	| otherwise = map (\x -> (x,c1)) [r1..r2]
getTuples (PAINT_SQUARE r c s) = (,) <$> [r-s..r+s] <*> [c-s..c+s]

isSolve :: Paint -> Bool
isSolve p = getLines p == getFill p

solve :: Paint -> [Command]
solve p = solve' p [] $ getReadyCommands p
		
solve' :: Paint -> [Command] -> [Command] -> [Command]
solve' p x [] = x
solve' p x (y:ys)
	| isSolve p = x
	| otherwise = solve' ap (y:x) (getOrderedCommands ap ys)
		where
			ap = applyCommand p y
