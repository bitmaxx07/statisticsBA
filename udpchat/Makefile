TARGET=udpchat
CC=gcc
CFLAGS=-Wall -Wextra -O2
LDFLAGS=
BUILDDIR=build

OBJECTS=build/udpchat.o

.PHONE: all clean

all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(CC) $(OBJECTS) $(LDFLAGS) -o $(TARGET)

$(BUILDDIR)/%.o: src/%.c $(BUILDDIR)/.empty
	$(CC) $(CFLAGS) $< -c -o $@

.PRECIOUS: $(BUILDDIR)/.empty

$(BUILDDIR)/.empty:
	@mkdir -p $(BUILDDIR)
	@touch $@

clean:
	-rm -rf $(OBJECTS)
	-rm -rf $(BUILDDIR)
	-rm -f $(TARGET)

