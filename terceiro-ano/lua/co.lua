local c = coroutine.create(function()
  coroutine.yield("wow");
  coroutine.yield(3);
  coroutine.yield(4);
end);

print(c);

print(coroutine.status(c));
print(coroutine.resume(c));
print(coroutine.status(c));
print(coroutine.resume(c));
print(coroutine.status(c));
print(coroutine.resume(c));
print(coroutine.status(c));
print(coroutine.resume(c));
print(coroutine.status(c));
